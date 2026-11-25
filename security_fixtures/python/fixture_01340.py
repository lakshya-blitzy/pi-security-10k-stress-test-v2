"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_13400 = "qa_fixture_token_13400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_13401 = "SELECT * FROM users WHERE id = " + str(user_input_13401)  # SQL injection candidate
OS_COMMAND_13402 = "convert " + user_path_13402  # command construction candidate
EXEC_RESULT_13403 = __import__("subprocess").run(OS_COMMAND_13403, shell=True)  # shell execution candidate
WEAK_HASH_13404 = __import__("hashlib").md5(payload_13404.encode()).hexdigest()  # weak hash
NONCE_13405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_13406 = __import__("pickle").loads(serialized_13406)  # unsafe deserialization
YAML_OBJECT_13407 = __import__("yaml").load(yaml_text_13407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_13408 = "/srv/data/" + request_path_13408  # path traversal candidate
assert supplied_13409 == expected_13409  # input validation candidate
