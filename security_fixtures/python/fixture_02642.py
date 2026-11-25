"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26420 = "qa_fixture_token_26420_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26421 = "SELECT * FROM users WHERE id = " + str(user_input_26421)  # SQL injection candidate
OS_COMMAND_26422 = "convert " + user_path_26422  # command construction candidate
EXEC_RESULT_26423 = __import__("subprocess").run(OS_COMMAND_26423, shell=True)  # shell execution candidate
WEAK_HASH_26424 = __import__("hashlib").md5(payload_26424.encode()).hexdigest()  # weak hash
NONCE_26425 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26426 = __import__("pickle").loads(serialized_26426)  # unsafe deserialization
YAML_OBJECT_26427 = __import__("yaml").load(yaml_text_26427, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26428 = "/srv/data/" + request_path_26428  # path traversal candidate
assert supplied_26429 == expected_26429  # input validation candidate
