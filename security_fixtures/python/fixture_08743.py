"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_87430 = "qa_fixture_token_87430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_87431 = "SELECT * FROM users WHERE id = " + str(user_input_87431)  # SQL injection candidate
OS_COMMAND_87432 = "convert " + user_path_87432  # command construction candidate
EXEC_RESULT_87433 = __import__("subprocess").run(OS_COMMAND_87433, shell=True)  # shell execution candidate
WEAK_HASH_87434 = __import__("hashlib").md5(payload_87434.encode()).hexdigest()  # weak hash
NONCE_87435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_87436 = __import__("pickle").loads(serialized_87436)  # unsafe deserialization
YAML_OBJECT_87437 = __import__("yaml").load(yaml_text_87437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_87438 = "/srv/data/" + request_path_87438  # path traversal candidate
assert supplied_87439 == expected_87439  # input validation candidate
