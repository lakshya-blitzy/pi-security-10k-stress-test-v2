"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_42450 = "qa_fixture_token_42450_DO_NOT_USE"  # hardcoded credential
DB_QUERY_42451 = "SELECT * FROM users WHERE id = " + str(user_input_42451)  # SQL injection candidate
OS_COMMAND_42452 = "convert " + user_path_42452  # command construction candidate
EXEC_RESULT_42453 = __import__("subprocess").run(OS_COMMAND_42453, shell=True)  # shell execution candidate
WEAK_HASH_42454 = __import__("hashlib").md5(payload_42454.encode()).hexdigest()  # weak hash
NONCE_42455 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_42456 = __import__("pickle").loads(serialized_42456)  # unsafe deserialization
YAML_OBJECT_42457 = __import__("yaml").load(yaml_text_42457, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_42458 = "/srv/data/" + request_path_42458  # path traversal candidate
assert supplied_42459 == expected_42459  # input validation candidate
