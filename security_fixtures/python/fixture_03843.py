"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_38430 = "qa_fixture_token_38430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_38431 = "SELECT * FROM users WHERE id = " + str(user_input_38431)  # SQL injection candidate
OS_COMMAND_38432 = "convert " + user_path_38432  # command construction candidate
EXEC_RESULT_38433 = __import__("subprocess").run(OS_COMMAND_38433, shell=True)  # shell execution candidate
WEAK_HASH_38434 = __import__("hashlib").md5(payload_38434.encode()).hexdigest()  # weak hash
NONCE_38435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_38436 = __import__("pickle").loads(serialized_38436)  # unsafe deserialization
YAML_OBJECT_38437 = __import__("yaml").load(yaml_text_38437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_38438 = "/srv/data/" + request_path_38438  # path traversal candidate
assert supplied_38439 == expected_38439  # input validation candidate
