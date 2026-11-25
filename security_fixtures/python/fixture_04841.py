"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48410 = "qa_fixture_token_48410_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48411 = "SELECT * FROM users WHERE id = " + str(user_input_48411)  # SQL injection candidate
OS_COMMAND_48412 = "convert " + user_path_48412  # command construction candidate
EXEC_RESULT_48413 = __import__("subprocess").run(OS_COMMAND_48413, shell=True)  # shell execution candidate
WEAK_HASH_48414 = __import__("hashlib").md5(payload_48414.encode()).hexdigest()  # weak hash
NONCE_48415 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48416 = __import__("pickle").loads(serialized_48416)  # unsafe deserialization
YAML_OBJECT_48417 = __import__("yaml").load(yaml_text_48417, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48418 = "/srv/data/" + request_path_48418  # path traversal candidate
assert supplied_48419 == expected_48419  # input validation candidate
