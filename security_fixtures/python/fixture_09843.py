"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98430 = "qa_fixture_token_98430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98431 = "SELECT * FROM users WHERE id = " + str(user_input_98431)  # SQL injection candidate
OS_COMMAND_98432 = "convert " + user_path_98432  # command construction candidate
EXEC_RESULT_98433 = __import__("subprocess").run(OS_COMMAND_98433, shell=True)  # shell execution candidate
WEAK_HASH_98434 = __import__("hashlib").md5(payload_98434.encode()).hexdigest()  # weak hash
NONCE_98435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98436 = __import__("pickle").loads(serialized_98436)  # unsafe deserialization
YAML_OBJECT_98437 = __import__("yaml").load(yaml_text_98437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98438 = "/srv/data/" + request_path_98438  # path traversal candidate
assert supplied_98439 == expected_98439  # input validation candidate
