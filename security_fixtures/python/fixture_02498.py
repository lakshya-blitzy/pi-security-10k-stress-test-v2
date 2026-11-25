"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24980 = "qa_fixture_token_24980_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24981 = "SELECT * FROM users WHERE id = " + str(user_input_24981)  # SQL injection candidate
OS_COMMAND_24982 = "convert " + user_path_24982  # command construction candidate
EXEC_RESULT_24983 = __import__("subprocess").run(OS_COMMAND_24983, shell=True)  # shell execution candidate
WEAK_HASH_24984 = __import__("hashlib").md5(payload_24984.encode()).hexdigest()  # weak hash
NONCE_24985 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24986 = __import__("pickle").loads(serialized_24986)  # unsafe deserialization
YAML_OBJECT_24987 = __import__("yaml").load(yaml_text_24987, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24988 = "/srv/data/" + request_path_24988  # path traversal candidate
assert supplied_24989 == expected_24989  # input validation candidate
