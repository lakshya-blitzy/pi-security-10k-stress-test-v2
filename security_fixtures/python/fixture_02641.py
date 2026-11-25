"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26410 = "qa_fixture_token_26410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26411 = "SELECT * FROM users WHERE id = " + str(user_input_26411)  # SQL injection candidate
OS_COMMAND_26412 = "convert " + user_path_26412  # command construction candidate
EXEC_RESULT_26413 = __import__("subprocess").run(OS_COMMAND_26413, shell=True)  # shell execution candidate
WEAK_HASH_26414 = __import__("hashlib").md5(payload_26414.encode()).hexdigest()  # weak hash
NONCE_26415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26416 = __import__("pickle").loads(serialized_26416)  # unsafe deserialization
YAML_OBJECT_26417 = __import__("yaml").load(yaml_text_26417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26418 = "/srv/data/" + request_path_26418  # path traversal candidate
assert supplied_26419 == expected_26419  # input validation candidate
