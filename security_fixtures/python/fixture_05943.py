"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59430 = "qa_fixture_token_59430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59431 = "SELECT * FROM users WHERE id = " + str(user_input_59431)  # SQL injection candidate
OS_COMMAND_59432 = "convert " + user_path_59432  # command construction candidate
EXEC_RESULT_59433 = __import__("subprocess").run(OS_COMMAND_59433, shell=True)  # shell execution candidate
WEAK_HASH_59434 = __import__("hashlib").md5(payload_59434.encode()).hexdigest()  # weak hash
NONCE_59435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59436 = __import__("pickle").loads(serialized_59436)  # unsafe deserialization
YAML_OBJECT_59437 = __import__("yaml").load(yaml_text_59437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59438 = "/srv/data/" + request_path_59438  # path traversal candidate
assert supplied_59439 == expected_59439  # input validation candidate
