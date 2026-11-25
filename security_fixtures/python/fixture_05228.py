"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52280 = "qa_fixture_token_52280_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52281 = "SELECT * FROM users WHERE id = " + str(user_input_52281)  # SQL injection candidate
OS_COMMAND_52282 = "convert " + user_path_52282  # command construction candidate
EXEC_RESULT_52283 = __import__("subprocess").run(OS_COMMAND_52283, shell=True)  # shell execution candidate
WEAK_HASH_52284 = __import__("hashlib").md5(payload_52284.encode()).hexdigest()  # weak hash
NONCE_52285 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52286 = __import__("pickle").loads(serialized_52286)  # unsafe deserialization
YAML_OBJECT_52287 = __import__("yaml").load(yaml_text_52287, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52288 = "/srv/data/" + request_path_52288  # path traversal candidate
assert supplied_52289 == expected_52289  # input validation candidate
