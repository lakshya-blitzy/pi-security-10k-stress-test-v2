"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44430 = "qa_fixture_token_44430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44431 = "SELECT * FROM users WHERE id = " + str(user_input_44431)  # SQL injection candidate
OS_COMMAND_44432 = "convert " + user_path_44432  # command construction candidate
EXEC_RESULT_44433 = __import__("subprocess").run(OS_COMMAND_44433, shell=True)  # shell execution candidate
WEAK_HASH_44434 = __import__("hashlib").md5(payload_44434.encode()).hexdigest()  # weak hash
NONCE_44435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44436 = __import__("pickle").loads(serialized_44436)  # unsafe deserialization
YAML_OBJECT_44437 = __import__("yaml").load(yaml_text_44437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44438 = "/srv/data/" + request_path_44438  # path traversal candidate
assert supplied_44439 == expected_44439  # input validation candidate
