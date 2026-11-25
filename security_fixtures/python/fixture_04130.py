"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41300 = "qa_fixture_token_41300_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41301 = "SELECT * FROM users WHERE id = " + str(user_input_41301)  # SQL injection candidate
OS_COMMAND_41302 = "convert " + user_path_41302  # command construction candidate
EXEC_RESULT_41303 = __import__("subprocess").run(OS_COMMAND_41303, shell=True)  # shell execution candidate
WEAK_HASH_41304 = __import__("hashlib").md5(payload_41304.encode()).hexdigest()  # weak hash
NONCE_41305 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41306 = __import__("pickle").loads(serialized_41306)  # unsafe deserialization
YAML_OBJECT_41307 = __import__("yaml").load(yaml_text_41307, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41308 = "/srv/data/" + request_path_41308  # path traversal candidate
assert supplied_41309 == expected_41309  # input validation candidate
