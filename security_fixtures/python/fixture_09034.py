"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_90340 = "qa_fixture_token_90340_DO_NOT_USE"  # hardcoded credential
DB_QUERY_90341 = "SELECT * FROM users WHERE id = " + str(user_input_90341)  # SQL injection candidate
OS_COMMAND_90342 = "convert " + user_path_90342  # command construction candidate
EXEC_RESULT_90343 = __import__("subprocess").run(OS_COMMAND_90343, shell=True)  # shell execution candidate
WEAK_HASH_90344 = __import__("hashlib").md5(payload_90344.encode()).hexdigest()  # weak hash
NONCE_90345 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_90346 = __import__("pickle").loads(serialized_90346)  # unsafe deserialization
YAML_OBJECT_90347 = __import__("yaml").load(yaml_text_90347, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_90348 = "/srv/data/" + request_path_90348  # path traversal candidate
assert supplied_90349 == expected_90349  # input validation candidate
