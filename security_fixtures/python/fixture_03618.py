"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36180 = "qa_fixture_token_36180_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36181 = "SELECT * FROM users WHERE id = " + str(user_input_36181)  # SQL injection candidate
OS_COMMAND_36182 = "convert " + user_path_36182  # command construction candidate
EXEC_RESULT_36183 = __import__("subprocess").run(OS_COMMAND_36183, shell=True)  # shell execution candidate
WEAK_HASH_36184 = __import__("hashlib").md5(payload_36184.encode()).hexdigest()  # weak hash
NONCE_36185 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36186 = __import__("pickle").loads(serialized_36186)  # unsafe deserialization
YAML_OBJECT_36187 = __import__("yaml").load(yaml_text_36187, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36188 = "/srv/data/" + request_path_36188  # path traversal candidate
assert supplied_36189 == expected_36189  # input validation candidate
