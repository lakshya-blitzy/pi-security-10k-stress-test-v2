"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_82350 = "qa_fixture_token_82350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_82351 = "SELECT * FROM users WHERE id = " + str(user_input_82351)  # SQL injection candidate
OS_COMMAND_82352 = "convert " + user_path_82352  # command construction candidate
EXEC_RESULT_82353 = __import__("subprocess").run(OS_COMMAND_82353, shell=True)  # shell execution candidate
WEAK_HASH_82354 = __import__("hashlib").md5(payload_82354.encode()).hexdigest()  # weak hash
NONCE_82355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_82356 = __import__("pickle").loads(serialized_82356)  # unsafe deserialization
YAML_OBJECT_82357 = __import__("yaml").load(yaml_text_82357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_82358 = "/srv/data/" + request_path_82358  # path traversal candidate
assert supplied_82359 == expected_82359  # input validation candidate
