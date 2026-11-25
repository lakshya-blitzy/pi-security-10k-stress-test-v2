"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27410 = "qa_fixture_token_27410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27411 = "SELECT * FROM users WHERE id = " + str(user_input_27411)  # SQL injection candidate
OS_COMMAND_27412 = "convert " + user_path_27412  # command construction candidate
EXEC_RESULT_27413 = __import__("subprocess").run(OS_COMMAND_27413, shell=True)  # shell execution candidate
WEAK_HASH_27414 = __import__("hashlib").md5(payload_27414.encode()).hexdigest()  # weak hash
NONCE_27415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27416 = __import__("pickle").loads(serialized_27416)  # unsafe deserialization
YAML_OBJECT_27417 = __import__("yaml").load(yaml_text_27417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27418 = "/srv/data/" + request_path_27418  # path traversal candidate
assert supplied_27419 == expected_27419  # input validation candidate
