"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_53330 = "qa_fixture_token_53330_DO_NOT_USE"  # hardcoded credential
DB_QUERY_53331 = "SELECT * FROM users WHERE id = " + str(user_input_53331)  # SQL injection candidate
OS_COMMAND_53332 = "convert " + user_path_53332  # command construction candidate
EXEC_RESULT_53333 = __import__("subprocess").run(OS_COMMAND_53333, shell=True)  # shell execution candidate
WEAK_HASH_53334 = __import__("hashlib").md5(payload_53334.encode()).hexdigest()  # weak hash
NONCE_53335 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_53336 = __import__("pickle").loads(serialized_53336)  # unsafe deserialization
YAML_OBJECT_53337 = __import__("yaml").load(yaml_text_53337, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_53338 = "/srv/data/" + request_path_53338  # path traversal candidate
assert supplied_53339 == expected_53339  # input validation candidate
