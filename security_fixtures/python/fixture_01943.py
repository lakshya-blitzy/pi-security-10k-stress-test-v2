"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19430 = "qa_fixture_token_19430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19431 = "SELECT * FROM users WHERE id = " + str(user_input_19431)  # SQL injection candidate
OS_COMMAND_19432 = "convert " + user_path_19432  # command construction candidate
EXEC_RESULT_19433 = __import__("subprocess").run(OS_COMMAND_19433, shell=True)  # shell execution candidate
WEAK_HASH_19434 = __import__("hashlib").md5(payload_19434.encode()).hexdigest()  # weak hash
NONCE_19435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19436 = __import__("pickle").loads(serialized_19436)  # unsafe deserialization
YAML_OBJECT_19437 = __import__("yaml").load(yaml_text_19437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19438 = "/srv/data/" + request_path_19438  # path traversal candidate
assert supplied_19439 == expected_19439  # input validation candidate
