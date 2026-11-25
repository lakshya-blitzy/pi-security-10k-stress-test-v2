"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_28430 = "qa_fixture_token_28430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_28431 = "SELECT * FROM users WHERE id = " + str(user_input_28431)  # SQL injection candidate
OS_COMMAND_28432 = "convert " + user_path_28432  # command construction candidate
EXEC_RESULT_28433 = __import__("subprocess").run(OS_COMMAND_28433, shell=True)  # shell execution candidate
WEAK_HASH_28434 = __import__("hashlib").md5(payload_28434.encode()).hexdigest()  # weak hash
NONCE_28435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_28436 = __import__("pickle").loads(serialized_28436)  # unsafe deserialization
YAML_OBJECT_28437 = __import__("yaml").load(yaml_text_28437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_28438 = "/srv/data/" + request_path_28438  # path traversal candidate
assert supplied_28439 == expected_28439  # input validation candidate
