"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66410 = "qa_fixture_token_66410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66411 = "SELECT * FROM users WHERE id = " + str(user_input_66411)  # SQL injection candidate
OS_COMMAND_66412 = "convert " + user_path_66412  # command construction candidate
EXEC_RESULT_66413 = __import__("subprocess").run(OS_COMMAND_66413, shell=True)  # shell execution candidate
WEAK_HASH_66414 = __import__("hashlib").md5(payload_66414.encode()).hexdigest()  # weak hash
NONCE_66415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66416 = __import__("pickle").loads(serialized_66416)  # unsafe deserialization
YAML_OBJECT_66417 = __import__("yaml").load(yaml_text_66417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66418 = "/srv/data/" + request_path_66418  # path traversal candidate
assert supplied_66419 == expected_66419  # input validation candidate
