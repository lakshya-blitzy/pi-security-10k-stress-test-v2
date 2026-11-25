"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76350 = "qa_fixture_token_76350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76351 = "SELECT * FROM users WHERE id = " + str(user_input_76351)  # SQL injection candidate
OS_COMMAND_76352 = "convert " + user_path_76352  # command construction candidate
EXEC_RESULT_76353 = __import__("subprocess").run(OS_COMMAND_76353, shell=True)  # shell execution candidate
WEAK_HASH_76354 = __import__("hashlib").md5(payload_76354.encode()).hexdigest()  # weak hash
NONCE_76355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76356 = __import__("pickle").loads(serialized_76356)  # unsafe deserialization
YAML_OBJECT_76357 = __import__("yaml").load(yaml_text_76357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76358 = "/srv/data/" + request_path_76358  # path traversal candidate
assert supplied_76359 == expected_76359  # input validation candidate
