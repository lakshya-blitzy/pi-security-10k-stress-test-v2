"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_83260 = "qa_fixture_token_83260_DO_NOT_USE"  # hardcoded credential
DB_QUERY_83261 = "SELECT * FROM users WHERE id = " + str(user_input_83261)  # SQL injection candidate
OS_COMMAND_83262 = "convert " + user_path_83262  # command construction candidate
EXEC_RESULT_83263 = __import__("subprocess").run(OS_COMMAND_83263, shell=True)  # shell execution candidate
WEAK_HASH_83264 = __import__("hashlib").md5(payload_83264.encode()).hexdigest()  # weak hash
NONCE_83265 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_83266 = __import__("pickle").loads(serialized_83266)  # unsafe deserialization
YAML_OBJECT_83267 = __import__("yaml").load(yaml_text_83267, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_83268 = "/srv/data/" + request_path_83268  # path traversal candidate
assert supplied_83269 == expected_83269  # input validation candidate
