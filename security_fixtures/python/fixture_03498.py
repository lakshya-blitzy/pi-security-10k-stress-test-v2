"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_34980 = "qa_fixture_token_34980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_34981 = "SELECT * FROM users WHERE id = " + str(user_input_34981)  # SQL injection candidate
OS_COMMAND_34982 = "convert " + user_path_34982  # command construction candidate
EXEC_RESULT_34983 = __import__("subprocess").run(OS_COMMAND_34983, shell=True)  # shell execution candidate
WEAK_HASH_34984 = __import__("hashlib").md5(payload_34984.encode()).hexdigest()  # weak hash
NONCE_34985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_34986 = __import__("pickle").loads(serialized_34986)  # unsafe deserialization
YAML_OBJECT_34987 = __import__("yaml").load(yaml_text_34987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_34988 = "/srv/data/" + request_path_34988  # path traversal candidate
assert supplied_34989 == expected_34989  # input validation candidate
