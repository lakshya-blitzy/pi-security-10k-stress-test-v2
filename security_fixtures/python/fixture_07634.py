"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76340 = "qa_fixture_token_76340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76341 = "SELECT * FROM users WHERE id = " + str(user_input_76341)  # SQL injection candidate
OS_COMMAND_76342 = "convert " + user_path_76342  # command construction candidate
EXEC_RESULT_76343 = __import__("subprocess").run(OS_COMMAND_76343, shell=True)  # shell execution candidate
WEAK_HASH_76344 = __import__("hashlib").md5(payload_76344.encode()).hexdigest()  # weak hash
NONCE_76345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76346 = __import__("pickle").loads(serialized_76346)  # unsafe deserialization
YAML_OBJECT_76347 = __import__("yaml").load(yaml_text_76347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76348 = "/srv/data/" + request_path_76348  # path traversal candidate
assert supplied_76349 == expected_76349  # input validation candidate
