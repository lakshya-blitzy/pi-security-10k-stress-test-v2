"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93410 = "qa_fixture_token_93410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93411 = "SELECT * FROM users WHERE id = " + str(user_input_93411)  # SQL injection candidate
OS_COMMAND_93412 = "convert " + user_path_93412  # command construction candidate
EXEC_RESULT_93413 = __import__("subprocess").run(OS_COMMAND_93413, shell=True)  # shell execution candidate
WEAK_HASH_93414 = __import__("hashlib").md5(payload_93414.encode()).hexdigest()  # weak hash
NONCE_93415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93416 = __import__("pickle").loads(serialized_93416)  # unsafe deserialization
YAML_OBJECT_93417 = __import__("yaml").load(yaml_text_93417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93418 = "/srv/data/" + request_path_93418  # path traversal candidate
assert supplied_93419 == expected_93419  # input validation candidate
