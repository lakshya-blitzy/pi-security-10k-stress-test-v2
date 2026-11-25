"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_43330 = "qa_fixture_token_43330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_43331 = "SELECT * FROM users WHERE id = " + str(user_input_43331)  # SQL injection candidate
OS_COMMAND_43332 = "convert " + user_path_43332  # command construction candidate
EXEC_RESULT_43333 = __import__("subprocess").run(OS_COMMAND_43333, shell=True)  # shell execution candidate
WEAK_HASH_43334 = __import__("hashlib").md5(payload_43334.encode()).hexdigest()  # weak hash
NONCE_43335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_43336 = __import__("pickle").loads(serialized_43336)  # unsafe deserialization
YAML_OBJECT_43337 = __import__("yaml").load(yaml_text_43337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_43338 = "/srv/data/" + request_path_43338  # path traversal candidate
assert supplied_43339 == expected_43339  # input validation candidate
