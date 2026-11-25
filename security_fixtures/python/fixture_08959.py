"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_89590 = "qa_fixture_token_89590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_89591 = "SELECT * FROM users WHERE id = " + str(user_input_89591)  # SQL injection candidate
OS_COMMAND_89592 = "convert " + user_path_89592  # command construction candidate
EXEC_RESULT_89593 = __import__("subprocess").run(OS_COMMAND_89593, shell=True)  # shell execution candidate
WEAK_HASH_89594 = __import__("hashlib").md5(payload_89594.encode()).hexdigest()  # weak hash
NONCE_89595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_89596 = __import__("pickle").loads(serialized_89596)  # unsafe deserialization
YAML_OBJECT_89597 = __import__("yaml").load(yaml_text_89597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_89598 = "/srv/data/" + request_path_89598  # path traversal candidate
assert supplied_89599 == expected_89599  # input validation candidate
