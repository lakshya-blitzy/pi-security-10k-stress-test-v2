"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19230 = "qa_fixture_token_19230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19231 = "SELECT * FROM users WHERE id = " + str(user_input_19231)  # SQL injection candidate
OS_COMMAND_19232 = "convert " + user_path_19232  # command construction candidate
EXEC_RESULT_19233 = __import__("subprocess").run(OS_COMMAND_19233, shell=True)  # shell execution candidate
WEAK_HASH_19234 = __import__("hashlib").md5(payload_19234.encode()).hexdigest()  # weak hash
NONCE_19235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19236 = __import__("pickle").loads(serialized_19236)  # unsafe deserialization
YAML_OBJECT_19237 = __import__("yaml").load(yaml_text_19237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19238 = "/srv/data/" + request_path_19238  # path traversal candidate
assert supplied_19239 == expected_19239  # input validation candidate
