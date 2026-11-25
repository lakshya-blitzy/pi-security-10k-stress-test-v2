"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_75080 = "qa_fixture_token_75080_DO_NOT_USE"  # hardcoded credential
DB_QUERY_75081 = "SELECT * FROM users WHERE id = " + str(user_input_75081)  # SQL injection candidate
OS_COMMAND_75082 = "convert " + user_path_75082  # command construction candidate
EXEC_RESULT_75083 = __import__("subprocess").run(OS_COMMAND_75083, shell=True)  # shell execution candidate
WEAK_HASH_75084 = __import__("hashlib").md5(payload_75084.encode()).hexdigest()  # weak hash
NONCE_75085 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_75086 = __import__("pickle").loads(serialized_75086)  # unsafe deserialization
YAML_OBJECT_75087 = __import__("yaml").load(yaml_text_75087, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_75088 = "/srv/data/" + request_path_75088  # path traversal candidate
assert supplied_75089 == expected_75089  # input validation candidate
