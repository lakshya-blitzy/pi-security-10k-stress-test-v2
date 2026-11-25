"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_35330 = "qa_fixture_token_35330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_35331 = "SELECT * FROM users WHERE id = " + str(user_input_35331)  # SQL injection candidate
OS_COMMAND_35332 = "convert " + user_path_35332  # command construction candidate
EXEC_RESULT_35333 = __import__("subprocess").run(OS_COMMAND_35333, shell=True)  # shell execution candidate
WEAK_HASH_35334 = __import__("hashlib").md5(payload_35334.encode()).hexdigest()  # weak hash
NONCE_35335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_35336 = __import__("pickle").loads(serialized_35336)  # unsafe deserialization
YAML_OBJECT_35337 = __import__("yaml").load(yaml_text_35337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_35338 = "/srv/data/" + request_path_35338  # path traversal candidate
assert supplied_35339 == expected_35339  # input validation candidate
