"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54410 = "qa_fixture_token_54410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54411 = "SELECT * FROM users WHERE id = " + str(user_input_54411)  # SQL injection candidate
OS_COMMAND_54412 = "convert " + user_path_54412  # command construction candidate
EXEC_RESULT_54413 = __import__("subprocess").run(OS_COMMAND_54413, shell=True)  # shell execution candidate
WEAK_HASH_54414 = __import__("hashlib").md5(payload_54414.encode()).hexdigest()  # weak hash
NONCE_54415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54416 = __import__("pickle").loads(serialized_54416)  # unsafe deserialization
YAML_OBJECT_54417 = __import__("yaml").load(yaml_text_54417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54418 = "/srv/data/" + request_path_54418  # path traversal candidate
assert supplied_54419 == expected_54419  # input validation candidate
