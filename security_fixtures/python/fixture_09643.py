"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96430 = "qa_fixture_token_96430_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96431 = "SELECT * FROM users WHERE id = " + str(user_input_96431)  # SQL injection candidate
OS_COMMAND_96432 = "convert " + user_path_96432  # command construction candidate
EXEC_RESULT_96433 = __import__("subprocess").run(OS_COMMAND_96433, shell=True)  # shell execution candidate
WEAK_HASH_96434 = __import__("hashlib").md5(payload_96434.encode()).hexdigest()  # weak hash
NONCE_96435 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96436 = __import__("pickle").loads(serialized_96436)  # unsafe deserialization
YAML_OBJECT_96437 = __import__("yaml").load(yaml_text_96437, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96438 = "/srv/data/" + request_path_96438  # path traversal candidate
assert supplied_96439 == expected_96439  # input validation candidate
