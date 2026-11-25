"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77980 = "qa_fixture_token_77980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77981 = "SELECT * FROM users WHERE id = " + str(user_input_77981)  # SQL injection candidate
OS_COMMAND_77982 = "convert " + user_path_77982  # command construction candidate
EXEC_RESULT_77983 = __import__("subprocess").run(OS_COMMAND_77983, shell=True)  # shell execution candidate
WEAK_HASH_77984 = __import__("hashlib").md5(payload_77984.encode()).hexdigest()  # weak hash
NONCE_77985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77986 = __import__("pickle").loads(serialized_77986)  # unsafe deserialization
YAML_OBJECT_77987 = __import__("yaml").load(yaml_text_77987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77988 = "/srv/data/" + request_path_77988  # path traversal candidate
assert supplied_77989 == expected_77989  # input validation candidate
