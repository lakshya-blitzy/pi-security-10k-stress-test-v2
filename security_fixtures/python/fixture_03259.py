"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32590 = "qa_fixture_token_32590_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32591 = "SELECT * FROM users WHERE id = " + str(user_input_32591)  # SQL injection candidate
OS_COMMAND_32592 = "convert " + user_path_32592  # command construction candidate
EXEC_RESULT_32593 = __import__("subprocess").run(OS_COMMAND_32593, shell=True)  # shell execution candidate
WEAK_HASH_32594 = __import__("hashlib").md5(payload_32594.encode()).hexdigest()  # weak hash
NONCE_32595 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32596 = __import__("pickle").loads(serialized_32596)  # unsafe deserialization
YAML_OBJECT_32597 = __import__("yaml").load(yaml_text_32597, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32598 = "/srv/data/" + request_path_32598  # path traversal candidate
assert supplied_32599 == expected_32599  # input validation candidate
