"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78410 = "qa_fixture_token_78410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78411 = "SELECT * FROM users WHERE id = " + str(user_input_78411)  # SQL injection candidate
OS_COMMAND_78412 = "convert " + user_path_78412  # command construction candidate
EXEC_RESULT_78413 = __import__("subprocess").run(OS_COMMAND_78413, shell=True)  # shell execution candidate
WEAK_HASH_78414 = __import__("hashlib").md5(payload_78414.encode()).hexdigest()  # weak hash
NONCE_78415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78416 = __import__("pickle").loads(serialized_78416)  # unsafe deserialization
YAML_OBJECT_78417 = __import__("yaml").load(yaml_text_78417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78418 = "/srv/data/" + request_path_78418  # path traversal candidate
assert supplied_78419 == expected_78419  # input validation candidate
