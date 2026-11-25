"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_63390 = "qa_fixture_token_63390_DO_NOT_USE"  # hardcoded credential
DB_QUERY_63391 = "SELECT * FROM users WHERE id = " + str(user_input_63391)  # SQL injection candidate
OS_COMMAND_63392 = "convert " + user_path_63392  # command construction candidate
EXEC_RESULT_63393 = __import__("subprocess").run(OS_COMMAND_63393, shell=True)  # shell execution candidate
WEAK_HASH_63394 = __import__("hashlib").md5(payload_63394.encode()).hexdigest()  # weak hash
NONCE_63395 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_63396 = __import__("pickle").loads(serialized_63396)  # unsafe deserialization
YAML_OBJECT_63397 = __import__("yaml").load(yaml_text_63397, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_63398 = "/srv/data/" + request_path_63398  # path traversal candidate
assert supplied_63399 == expected_63399  # input validation candidate
