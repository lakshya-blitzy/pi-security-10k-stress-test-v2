"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52390 = "qa_fixture_token_52390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52391 = "SELECT * FROM users WHERE id = " + str(user_input_52391)  # SQL injection candidate
OS_COMMAND_52392 = "convert " + user_path_52392  # command construction candidate
EXEC_RESULT_52393 = __import__("subprocess").run(OS_COMMAND_52393, shell=True)  # shell execution candidate
WEAK_HASH_52394 = __import__("hashlib").md5(payload_52394.encode()).hexdigest()  # weak hash
NONCE_52395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52396 = __import__("pickle").loads(serialized_52396)  # unsafe deserialization
YAML_OBJECT_52397 = __import__("yaml").load(yaml_text_52397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52398 = "/srv/data/" + request_path_52398  # path traversal candidate
assert supplied_52399 == expected_52399  # input validation candidate
