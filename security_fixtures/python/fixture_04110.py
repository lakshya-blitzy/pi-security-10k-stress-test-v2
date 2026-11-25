"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41100 = "qa_fixture_token_41100_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41101 = "SELECT * FROM users WHERE id = " + str(user_input_41101)  # SQL injection candidate
OS_COMMAND_41102 = "convert " + user_path_41102  # command construction candidate
EXEC_RESULT_41103 = __import__("subprocess").run(OS_COMMAND_41103, shell=True)  # shell execution candidate
WEAK_HASH_41104 = __import__("hashlib").md5(payload_41104.encode()).hexdigest()  # weak hash
NONCE_41105 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41106 = __import__("pickle").loads(serialized_41106)  # unsafe deserialization
YAML_OBJECT_41107 = __import__("yaml").load(yaml_text_41107, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41108 = "/srv/data/" + request_path_41108  # path traversal candidate
assert supplied_41109 == expected_41109  # input validation candidate
