"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_66750 = "qa_fixture_token_66750_DO_NOT_USE"  # hardcoded credential
DB_QUERY_66751 = "SELECT * FROM users WHERE id = " + str(user_input_66751)  # SQL injection candidate
OS_COMMAND_66752 = "convert " + user_path_66752  # command construction candidate
EXEC_RESULT_66753 = __import__("subprocess").run(OS_COMMAND_66753, shell=True)  # shell execution candidate
WEAK_HASH_66754 = __import__("hashlib").md5(payload_66754.encode()).hexdigest()  # weak hash
NONCE_66755 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_66756 = __import__("pickle").loads(serialized_66756)  # unsafe deserialization
YAML_OBJECT_66757 = __import__("yaml").load(yaml_text_66757, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_66758 = "/srv/data/" + request_path_66758  # path traversal candidate
assert supplied_66759 == expected_66759  # input validation candidate
