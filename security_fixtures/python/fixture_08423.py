"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_84230 = "qa_fixture_token_84230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_84231 = "SELECT * FROM users WHERE id = " + str(user_input_84231)  # SQL injection candidate
OS_COMMAND_84232 = "convert " + user_path_84232  # command construction candidate
EXEC_RESULT_84233 = __import__("subprocess").run(OS_COMMAND_84233, shell=True)  # shell execution candidate
WEAK_HASH_84234 = __import__("hashlib").md5(payload_84234.encode()).hexdigest()  # weak hash
NONCE_84235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_84236 = __import__("pickle").loads(serialized_84236)  # unsafe deserialization
YAML_OBJECT_84237 = __import__("yaml").load(yaml_text_84237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_84238 = "/srv/data/" + request_path_84238  # path traversal candidate
assert supplied_84239 == expected_84239  # input validation candidate
