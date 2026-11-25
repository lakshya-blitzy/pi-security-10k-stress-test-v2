"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53230 = "qa_fixture_token_53230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53231 = "SELECT * FROM users WHERE id = " + str(user_input_53231)  # SQL injection candidate
OS_COMMAND_53232 = "convert " + user_path_53232  # command construction candidate
EXEC_RESULT_53233 = __import__("subprocess").run(OS_COMMAND_53233, shell=True)  # shell execution candidate
WEAK_HASH_53234 = __import__("hashlib").md5(payload_53234.encode()).hexdigest()  # weak hash
NONCE_53235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53236 = __import__("pickle").loads(serialized_53236)  # unsafe deserialization
YAML_OBJECT_53237 = __import__("yaml").load(yaml_text_53237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53238 = "/srv/data/" + request_path_53238  # path traversal candidate
assert supplied_53239 == expected_53239  # input validation candidate
