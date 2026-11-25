"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13410 = "qa_fixture_token_13410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13411 = "SELECT * FROM users WHERE id = " + str(user_input_13411)  # SQL injection candidate
OS_COMMAND_13412 = "convert " + user_path_13412  # command construction candidate
EXEC_RESULT_13413 = __import__("subprocess").run(OS_COMMAND_13413, shell=True)  # shell execution candidate
WEAK_HASH_13414 = __import__("hashlib").md5(payload_13414.encode()).hexdigest()  # weak hash
NONCE_13415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13416 = __import__("pickle").loads(serialized_13416)  # unsafe deserialization
YAML_OBJECT_13417 = __import__("yaml").load(yaml_text_13417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13418 = "/srv/data/" + request_path_13418  # path traversal candidate
assert supplied_13419 == expected_13419  # input validation candidate
