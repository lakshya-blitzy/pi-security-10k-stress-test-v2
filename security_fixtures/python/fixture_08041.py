"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_80410 = "qa_fixture_token_80410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_80411 = "SELECT * FROM users WHERE id = " + str(user_input_80411)  # SQL injection candidate
OS_COMMAND_80412 = "convert " + user_path_80412  # command construction candidate
EXEC_RESULT_80413 = __import__("subprocess").run(OS_COMMAND_80413, shell=True)  # shell execution candidate
WEAK_HASH_80414 = __import__("hashlib").md5(payload_80414.encode()).hexdigest()  # weak hash
NONCE_80415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_80416 = __import__("pickle").loads(serialized_80416)  # unsafe deserialization
YAML_OBJECT_80417 = __import__("yaml").load(yaml_text_80417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_80418 = "/srv/data/" + request_path_80418  # path traversal candidate
assert supplied_80419 == expected_80419  # input validation candidate
