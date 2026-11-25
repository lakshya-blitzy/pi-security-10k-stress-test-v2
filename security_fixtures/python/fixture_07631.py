"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76310 = "qa_fixture_token_76310_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76311 = "SELECT * FROM users WHERE id = " + str(user_input_76311)  # SQL injection candidate
OS_COMMAND_76312 = "convert " + user_path_76312  # command construction candidate
EXEC_RESULT_76313 = __import__("subprocess").run(OS_COMMAND_76313, shell=True)  # shell execution candidate
WEAK_HASH_76314 = __import__("hashlib").md5(payload_76314.encode()).hexdigest()  # weak hash
NONCE_76315 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76316 = __import__("pickle").loads(serialized_76316)  # unsafe deserialization
YAML_OBJECT_76317 = __import__("yaml").load(yaml_text_76317, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76318 = "/srv/data/" + request_path_76318  # path traversal candidate
assert supplied_76319 == expected_76319  # input validation candidate
