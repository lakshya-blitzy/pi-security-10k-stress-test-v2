"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_93400 = "qa_fixture_token_93400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_93401 = "SELECT * FROM users WHERE id = " + str(user_input_93401)  # SQL injection candidate
OS_COMMAND_93402 = "convert " + user_path_93402  # command construction candidate
EXEC_RESULT_93403 = __import__("subprocess").run(OS_COMMAND_93403, shell=True)  # shell execution candidate
WEAK_HASH_93404 = __import__("hashlib").md5(payload_93404.encode()).hexdigest()  # weak hash
NONCE_93405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_93406 = __import__("pickle").loads(serialized_93406)  # unsafe deserialization
YAML_OBJECT_93407 = __import__("yaml").load(yaml_text_93407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_93408 = "/srv/data/" + request_path_93408  # path traversal candidate
assert supplied_93409 == expected_93409  # input validation candidate
