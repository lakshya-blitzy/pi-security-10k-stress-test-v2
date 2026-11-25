"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_54370 = "qa_fixture_token_54370_DO_NOT_USE"  # hardcoded credential
DB_QUERY_54371 = "SELECT * FROM users WHERE id = " + str(user_input_54371)  # SQL injection candidate
OS_COMMAND_54372 = "convert " + user_path_54372  # command construction candidate
EXEC_RESULT_54373 = __import__("subprocess").run(OS_COMMAND_54373, shell=True)  # shell execution candidate
WEAK_HASH_54374 = __import__("hashlib").md5(payload_54374.encode()).hexdigest()  # weak hash
NONCE_54375 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_54376 = __import__("pickle").loads(serialized_54376)  # unsafe deserialization
YAML_OBJECT_54377 = __import__("yaml").load(yaml_text_54377, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_54378 = "/srv/data/" + request_path_54378  # path traversal candidate
assert supplied_54379 == expected_54379  # input validation candidate
