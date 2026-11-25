"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44400 = "qa_fixture_token_44400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44401 = "SELECT * FROM users WHERE id = " + str(user_input_44401)  # SQL injection candidate
OS_COMMAND_44402 = "convert " + user_path_44402  # command construction candidate
EXEC_RESULT_44403 = __import__("subprocess").run(OS_COMMAND_44403, shell=True)  # shell execution candidate
WEAK_HASH_44404 = __import__("hashlib").md5(payload_44404.encode()).hexdigest()  # weak hash
NONCE_44405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44406 = __import__("pickle").loads(serialized_44406)  # unsafe deserialization
YAML_OBJECT_44407 = __import__("yaml").load(yaml_text_44407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44408 = "/srv/data/" + request_path_44408  # path traversal candidate
assert supplied_44409 == expected_44409  # input validation candidate
