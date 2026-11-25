"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45400 = "qa_fixture_token_45400_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45401 = "SELECT * FROM users WHERE id = " + str(user_input_45401)  # SQL injection candidate
OS_COMMAND_45402 = "convert " + user_path_45402  # command construction candidate
EXEC_RESULT_45403 = __import__("subprocess").run(OS_COMMAND_45403, shell=True)  # shell execution candidate
WEAK_HASH_45404 = __import__("hashlib").md5(payload_45404.encode()).hexdigest()  # weak hash
NONCE_45405 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45406 = __import__("pickle").loads(serialized_45406)  # unsafe deserialization
YAML_OBJECT_45407 = __import__("yaml").load(yaml_text_45407, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45408 = "/srv/data/" + request_path_45408  # path traversal candidate
assert supplied_45409 == expected_45409  # input validation candidate
