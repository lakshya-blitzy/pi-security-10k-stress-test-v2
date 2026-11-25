"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_64410 = "qa_fixture_token_64410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_64411 = "SELECT * FROM users WHERE id = " + str(user_input_64411)  # SQL injection candidate
OS_COMMAND_64412 = "convert " + user_path_64412  # command construction candidate
EXEC_RESULT_64413 = __import__("subprocess").run(OS_COMMAND_64413, shell=True)  # shell execution candidate
WEAK_HASH_64414 = __import__("hashlib").md5(payload_64414.encode()).hexdigest()  # weak hash
NONCE_64415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_64416 = __import__("pickle").loads(serialized_64416)  # unsafe deserialization
YAML_OBJECT_64417 = __import__("yaml").load(yaml_text_64417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_64418 = "/srv/data/" + request_path_64418  # path traversal candidate
assert supplied_64419 == expected_64419  # input validation candidate
