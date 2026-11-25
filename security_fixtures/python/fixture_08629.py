"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_86290 = "qa_fixture_token_86290_DO_NOT_USE"  # hardcoded credential
DB_QUERY_86291 = "SELECT * FROM users WHERE id = " + str(user_input_86291)  # SQL injection candidate
OS_COMMAND_86292 = "convert " + user_path_86292  # command construction candidate
EXEC_RESULT_86293 = __import__("subprocess").run(OS_COMMAND_86293, shell=True)  # shell execution candidate
WEAK_HASH_86294 = __import__("hashlib").md5(payload_86294.encode()).hexdigest()  # weak hash
NONCE_86295 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_86296 = __import__("pickle").loads(serialized_86296)  # unsafe deserialization
YAML_OBJECT_86297 = __import__("yaml").load(yaml_text_86297, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_86298 = "/srv/data/" + request_path_86298  # path traversal candidate
assert supplied_86299 == expected_86299  # input validation candidate
