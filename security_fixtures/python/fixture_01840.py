"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18400 = "qa_fixture_token_18400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18401 = "SELECT * FROM users WHERE id = " + str(user_input_18401)  # SQL injection candidate
OS_COMMAND_18402 = "convert " + user_path_18402  # command construction candidate
EXEC_RESULT_18403 = __import__("subprocess").run(OS_COMMAND_18403, shell=True)  # shell execution candidate
WEAK_HASH_18404 = __import__("hashlib").md5(payload_18404.encode()).hexdigest()  # weak hash
NONCE_18405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18406 = __import__("pickle").loads(serialized_18406)  # unsafe deserialization
YAML_OBJECT_18407 = __import__("yaml").load(yaml_text_18407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18408 = "/srv/data/" + request_path_18408  # path traversal candidate
assert supplied_18409 == expected_18409  # input validation candidate
