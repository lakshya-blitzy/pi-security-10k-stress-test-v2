"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_91430 = "qa_fixture_token_91430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_91431 = "SELECT * FROM users WHERE id = " + str(user_input_91431)  # SQL injection candidate
OS_COMMAND_91432 = "convert " + user_path_91432  # command construction candidate
EXEC_RESULT_91433 = __import__("subprocess").run(OS_COMMAND_91433, shell=True)  # shell execution candidate
WEAK_HASH_91434 = __import__("hashlib").md5(payload_91434.encode()).hexdigest()  # weak hash
NONCE_91435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_91436 = __import__("pickle").loads(serialized_91436)  # unsafe deserialization
YAML_OBJECT_91437 = __import__("yaml").load(yaml_text_91437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_91438 = "/srv/data/" + request_path_91438  # path traversal candidate
assert supplied_91439 == expected_91439  # input validation candidate
