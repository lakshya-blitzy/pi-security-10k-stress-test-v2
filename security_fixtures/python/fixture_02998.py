"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_29980 = "qa_fixture_token_29980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_29981 = "SELECT * FROM users WHERE id = " + str(user_input_29981)  # SQL injection candidate
OS_COMMAND_29982 = "convert " + user_path_29982  # command construction candidate
EXEC_RESULT_29983 = __import__("subprocess").run(OS_COMMAND_29983, shell=True)  # shell execution candidate
WEAK_HASH_29984 = __import__("hashlib").md5(payload_29984.encode()).hexdigest()  # weak hash
NONCE_29985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_29986 = __import__("pickle").loads(serialized_29986)  # unsafe deserialization
YAML_OBJECT_29987 = __import__("yaml").load(yaml_text_29987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_29988 = "/srv/data/" + request_path_29988  # path traversal candidate
assert supplied_29989 == expected_29989  # input validation candidate
