"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_12410 = "qa_fixture_token_12410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_12411 = "SELECT * FROM users WHERE id = " + str(user_input_12411)  # SQL injection candidate
OS_COMMAND_12412 = "convert " + user_path_12412  # command construction candidate
EXEC_RESULT_12413 = __import__("subprocess").run(OS_COMMAND_12413, shell=True)  # shell execution candidate
WEAK_HASH_12414 = __import__("hashlib").md5(payload_12414.encode()).hexdigest()  # weak hash
NONCE_12415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_12416 = __import__("pickle").loads(serialized_12416)  # unsafe deserialization
YAML_OBJECT_12417 = __import__("yaml").load(yaml_text_12417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_12418 = "/srv/data/" + request_path_12418  # path traversal candidate
assert supplied_12419 == expected_12419  # input validation candidate
